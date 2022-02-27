import copy
import datetime
import time

config = {
"nlp_similar_text_deduplicate_feed": {
"search_max_waiting_time": 2,
"add_max_batch_size": 256,
"add_max_waiting_time": 3,
"search_max_batch_size": 512
},
"nlp_similartext_im_prep_va_test": {
"search_max_waiting_time": 0.08,
"add_max_batch_size": 1024,
"add_max_waiting_time": 2,
"search_max_batch_size": 512
},
"nlp_similartext_im_prep_va": {
"search_max_waiting_time": 0.08,
"add_max_batch_size": 1024,
"add_max_waiting_time": 2,
"search_max_batch_size": 512
},
"nlp_similartext_comment_prep_va": {
"search_max_waiting_time": 0.08,
"add_max_batch_size": 1024,
"add_max_waiting_time": 2,
"search_max_batch_size": 512
},
"nlp_similartext_comment_prep_va_test": {
"search_max_waiting_time": 0.08,
"add_max_batch_size": 1024,
"add_max_waiting_time": 2,
"search_max_batch_size": 512
},
"avatar_aggregation_v4": {
"search_max_waiting_time": 3,
"add_max_batch_size": 1024,
"add_max_waiting_time": 2,
"search_max_batch_size": 512
},
"feedimage_aggregation_v4": {
"search_max_waiting_time": 3,
"add_max_batch_size": 1024,
"add_max_waiting_time": 2,
"search_max_batch_size": 512
},
"feedvideo_aggregation_v4": {
"search_max_waiting_time": 3,
"add_max_batch_size": 1024,
"add_max_waiting_time": 2,
"search_max_batch_size": 512
},
"hezi_feedimage_aggregation_v4": {
"search_max_waiting_time": 3,
"add_max_batch_size": 1024,
"add_max_waiting_time": 2,
"search_max_batch_size": 512
}
}


def get_business_batch_config(configure):
    """
    遍历business的配置并以dict形式返回
    :return:dict {'business':config}
    """
    business_batch_config = {
        'default': {
            'add_max_waiting_time': 1.0,
            'add_max_batch_size': 256,
            'search_max_waiting_time': 1.0,
            'search_max_batch_size': 1024}}
    try:
        for business, config in configure.items():
            for config_k, config_v in config.items():
                if config_k in ["add_max_waiting_time", "add_max_batch_size", "search_max_waiting_time",
                                "search_max_batch_size"]:
                    if business not in business_batch_config:
                        business_batch_config[business] = {}
                    business_batch_config[business][config_k] = config_v
    except Exception:
        print('get business config exception')
    # print('business batch config:{}'.format(business_batch_config))
    return business_batch_config


def get_business_batch_config2(configure):
    """
    遍历business的配置并以dict形式返回
    :return:dict {'business':config}
    """
    check_set = {"add_max_waiting_time", "add_max_batch_size", "search_max_waiting_time", "search_max_batch_size"}
    default_config = {'add_max_waiting_time': 1.0, 'add_max_batch_size': 256, 'search_max_waiting_time': 1.0,
                      'search_max_batch_size': 1024}
    business_batch_config = {
        'default': default_config}
    try:
        for business, config in configure.items():
            business_batch_config[business] = copy.copy(default_config)
            # print(type(config))
            business_batch_config[business].update({k: v for k, v in config.items() if k in check_set})
    except Exception as e:
        print('get business config exception')
        print(e)
    # print('business batch config:{}'.format(business_batch_config))
    return business_batch_config


time.sleep(1)
access_start = datetime.datetime.now()
for i in range(10000):
    b = get_business_batch_config(config)
endtime = datetime.datetime.now()
print((endtime - access_start).microseconds)

access_start = datetime.datetime.now()
for i in range(10000):
    a = get_business_batch_config2(config)
endtime = datetime.datetime.now()
print((endtime - access_start).microseconds)

access_start = datetime.datetime.now()
for i in range(10000):
    b = get_business_batch_config(config)
endtime = datetime.datetime.now()
print((endtime - access_start).microseconds)

access_start = datetime.datetime.now()
for i in range(10000):
    a = get_business_batch_config2(config)
endtime = datetime.datetime.now()
print((endtime - access_start).microseconds)

# configure = get_business_batch_config2(config)
# for k, v in configure.items():
#     print(k, v)
