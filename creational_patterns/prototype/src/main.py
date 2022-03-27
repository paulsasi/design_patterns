import configuration
import copy

if __name__ == '__main__':

    
    urls = ["url1", "url2"]
    hosts = [["host1, host2"]]

    config = configuration.Configuration(urls=urls, hosts=hosts)

    config_copy = copy.copy(config)
    config_deep_copy = copy.deepcopy(config)

    print(config.urls)
    print(config.hosts)
    
    print('#####')

    print(config_copy.urls)
    print(config_copy.hosts)

    print('#####')

    print(config_deep_copy.urls)
    print(config_deep_copy.hosts)

    print('########### CHANGE URLS #############')
    config.urls.append("url3")


    print(config.urls)
    print(config.hosts)
    
    print('#####')

    print(config_copy.urls)
    print(config_copy.hosts)

    print('#####')

    print(config_deep_copy.urls)
    print(config_deep_copy.hosts)

    print('########### CHANGE HOSTS #############')
    config.hosts[0].append("host3")


    print(config.urls)
    print(config.hosts)
    
    print('#####')

    print(config_copy.urls)
    print(config_copy.hosts)

    print('#####')

    print(config_deep_copy.urls)
    print(config_deep_copy.hosts)
