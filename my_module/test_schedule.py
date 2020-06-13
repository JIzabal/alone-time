"""Test for my functions."""


from schedule import read_file, get_schedules, find_free_time

# Inputs and expected values used in tests
schedule = ['10:00a-10:50a', '11:00a-11:50a', '6:00p-8:00p', 
    '#', '9:00a-9:50a', '10:00a-10:50a', '11:00a-11:50a', '2:00p-4:00p']
schedule_1 = ['10:00a-10:50a', '11:00a-11:50a', '6:00p-8:00p']
schedule_2 = ['9:00a-9:50a', '10:00a-10:50a', '11:00a-11:50a', '2:00p-4:00p']

def test_read_file():
  
  assert callable(read_file)
  assert isinstance(read_file('my_module/test-schedules-1.txt'), list)
  assert read_file('my_module/test-schedules-1.txt') == schedule


def test_get_schedules():
  
  assert callable(get_schedules)
  assert isinstance(get_schedules(schedule), tuple)
  assert get_schedules(schedule) == (schedule_1, schedule_2)
    

def test_find_free_time():
  
  assert callable(find_free_time)


                 
    