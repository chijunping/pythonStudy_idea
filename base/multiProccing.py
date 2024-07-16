from multiprocessing.dummy import Pool as ThreadPool
import time


def fun(n):
    time.sleep(2)


start = time.time()
for i in range(5):
    fun(i)
print("���߳�˳��ִ�к�ʱ:", time.time() - start)

start2 = time.time()
# ��8�� worker��û�в���ʱĬ���� cpu �ĺ�����
pool = ThreadPool(processes=5)
# ���߳���ִ�� urllib2.urlopen(url) ������ִ�н��
results2 = pool.map(fun, range(5))
pool.close()
pool.join()
print("�̳߳أ�5������ִ�к�ʱ:", time.time() - start2)
