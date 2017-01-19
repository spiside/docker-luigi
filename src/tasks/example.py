import time

import luigi
from luigi.local_target import LocalTarget


class RunAllTasks(luigi.Task):

    def requires(self):
        for i in range(10):
            yield RunExampleTask(i)

    def run(self):
        with self.output().open('w') as f:
            f.write('All done!')

    def output(self):
        return LocalTarget('tmp/RunAllTasks.txt')


class RunExampleTask(luigi.Task):
    number = luigi.IntParameter()

    def run(self):
        time.sleep(self.number)

        with self.output().open('w') as f:
            f.write("This is task # {}".format(self.number))

    def output(self):
        return LocalTarget('tmp/runExampleTask_{}.txt'.format(self.number))


if __name__ == "__main__":
    luigi.run()
