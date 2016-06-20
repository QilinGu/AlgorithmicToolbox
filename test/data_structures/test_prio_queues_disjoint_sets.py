import pytest
import data_structures.prio_queues_disjoint_sets.build_heap as build_heap
import data_structures.prio_queues_disjoint_sets.job_queue as job_queue


@pytest.mark.timeout(3)
class TestBuildHeap:
    def check_heap(self, a):
        for i in range(len(a)):
            if 2 * i + 1 < len(a):
                assert a[i] < a[2 * i + 1]
            if 2 * i + 2 < len(a):
                assert a[i] < a[2 * i + 2]

    def test_sample1(self):
        test_input = [5, 4, 3, 2, 1]
        heap = build_heap.HeapBuilder(test_input)
        heap.generate_swaps()
        self.check_heap(heap.data)
        assert len(heap.swaps) <= 4 * len(test_input)

    def test_worst_case(self):
        test_input = list(reversed(range(1, 100000 + 1)))
        heap = build_heap.HeapBuilder(test_input)
        heap.generate_swaps()
        self.check_heap(heap.data)
        assert len(heap.swaps) <= 4 * len(test_input)


@pytest.mark.timeout(6)
class TestJobQueue:
    def test_sample1(self):
        jobs = [1, 2, 3, 4, 5]
        threads = 2
        jq = job_queue.JobQueue(threads, jobs)
        jq.assign_jobs()
        assert jq.assigned_workers == [0, 1, 0, 1, 0]
        assert jq.start_times == [0, 0, 1, 2, 4]
