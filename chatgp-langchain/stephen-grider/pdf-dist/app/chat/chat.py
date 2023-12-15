from langchain.chat_models import ChatOpenAI

from app.chat.chains.retrieval import StreamingConversationalRetrievalChain
from app.chat.llms import llm_map
from app.chat.memories import memory_map
from app.chat.models import ChatArgs
from app.chat.score import random_component_by_score
from app.chat.vector_stores import retriever_map
from app.web.api import get_conversation_components, set_conversation_components
from app.chat.tracing.langfuse import langfuse
from langfuse.model import CreateTrace


def select_component(component_type, component_map, chat_args):
    components = get_conversation_components(chat_args.conversation_id)
    previous_component = components[component_type]

    if previous_component:
        builder = component_map[previous_component]
        return previous_component, builder(chat_args)

    random_name = random_component_by_score(component_type, component_map)
    builder = component_map[random_name]
    return random_name, builder(chat_args)


def build_chat(chat_args: ChatArgs):
    retriever_name, retriever = select_component(
        "retriever",
        retriever_map,
        chat_args,
    )
    llm_name, llm = select_component(
        "llm",
        llm_map,
        chat_args,
    )
    memory_name, memory = select_component(
        "memory",
        memory_map,
        chat_args,
    )

    # For some reason, the second question is not using another retriever component
    # Input: What country produces the most spice?
    # Output: Running chain with: memory: sql_buffer_memory, llm: gpt-4, retriever: pinecone_1
    # Input: and second?
    # Output: Running chain with: memory: sql_buffer_memory, llm: gpt-4, retriever: pinecone_1
    print(
        f"Running chain with: memory: {memory_name}, llm: {llm_name}, retriever: {retriever_name}"
    )

    set_conversation_components(
        chat_args.conversation_id,
        llm=llm_name,
        retriever=retriever_name,
        memory=memory_name,
    )

    condense_question_llm = ChatOpenAI(streaming=False)

    trace = langfuse.trace(
        CreateTrace(
            id=chat_args.conversation_id,
            metadata=chat_args.metadata,
        )
    )

    return StreamingConversationalRetrievalChain.from_llm(
        llm=llm,
        condense_question_llm=condense_question_llm,
        memory=memory,
        retriever=retriever,
        callbacks=[trace.getNewHandler()],
    )
