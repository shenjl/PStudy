#例5 利用yield from语句向生成器（协程）传送数据
#传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。
#如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，换回生产者继续生产，效率极高
import time
def consumer_work(len):
    # 读取send传进的数据，并模拟进行处理数据
    print("writer:")    
    w=''
    while True:
        w = yield w    # w接收send传进的数据,同时也是返回的数据
        print('[CONSUMER] Consuming %s...>> ', w)
        w*=len #将返回的数据乘以100
        time.sleep(0.1)
def consumer(coro):
    yield from coro#将数据传递到协程(生成器)对象中
 
 
def produce(c):
    c.send(None)# "prime" the coroutine
    for i in range(5):
        print('[Produce] Producing %s----', i)
        w=c.send(i)#发送完成后进入协程中执行
        print('[Produce] receive %s----', w)
    c.close()

c1=consumer_work(100)
produce(consumer(c1))