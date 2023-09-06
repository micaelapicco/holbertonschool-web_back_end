
#!/usr/bin/env python3
"""
Task 11:
returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    topic_list = []
    topics = mongo_collection.find({"topic": topic})
    for topic in topics:
        topic_list.append(topic)
    return topic_list
