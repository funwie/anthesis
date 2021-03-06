
class Period:

  def __init__(self, start, end):
    self.start =  start
    self.end = end
    self.points = []
    self.point_count = 0

  def has_valid_points(self):
    pass

  def __repr__(self):
    return f'Start: {self.start} End: {self.end} Points: {self.points}, point_count: {self.point_count}'

  def __str__(self):
    return f'Start: {self.start} End: {self.end} Points: {self.points}, point_count: {self.point_count}'
  
def generate_periods(period_list):

    if not period_list:
      raise ValueError('Periods required')

    periods_size = len(period_list)
    
    if periods_size % 2 == 1:
      raise ValueError('Invalid periods')

    if periods_size > 20:
      raise ValueError('Periods exceed maximum of 10')

    periods = []
    for i in range(1, periods_size, 2):
      start = min(period_list[i-1], period_list[i])
      end = max(period_list[i-1], period_list[i])

      if start > 0 and end > 0:
        period = Period(start, end)
        periods.append(period)
      else:
        # Log
        print(f'Invalid period {start} - {end}')
    return periods


def populate_points(periods, points):

  if not periods or not points:
    raise ValueError('Points and periods required')

  valid_point_periods = []

  for period in periods:
    period_points = [point for point in points if point >= period.start and point <= period.end]
    point_count = sum(period_points)
    if period_points and len(period_points) <= 10:
      period.points = period_points
      period.point_count = point_count
      valid_point_periods.append(period)
  return valid_point_periods


input_periods = [1, 5, 6, 10, 11, 20, 21, 25, 26, 40, 41, 50]
input_points = [14, 9, 24, 2, 44, 8, 41, 4, 46, 26, 11, 31, 18, 24, 21, 4, 22, 50, 6, 36]
sorted_points = sorted(input_points)

valid_periods = generate_periods(input_periods)
periods_with_valid_points = populate_points(valid_periods, sorted_points)

print(periods_with_valid_points)

