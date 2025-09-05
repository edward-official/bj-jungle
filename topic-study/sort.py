# I'm a developer who hates snake_case but I follow the standard
class MergeSorter:
  @staticmethod
  def operate(target_elements):
    MergeSorter._merge_sort(target_elements, [None] * len(target_elements), 0, len(target_elements)-1)
    return

  @staticmethod
  def _merge_sort(target_elements, temporal_elements, opening_index: int, closing_index: int):
    if opening_index==closing_index:
      return
    center_index = (opening_index + closing_index) // 2
    MergeSorter._merge_sort(target_elements, temporal_elements, opening_index, center_index)
    MergeSorter._merge_sort(target_elements, temporal_elements, center_index+1, closing_index)
    MergeSorter._merge(target_elements, temporal_elements, opening_index, closing_index)
    return

  @staticmethod
  def _merge(target_elements, temporal_elements, opening_index: int, closing_index: int):
    center_index = (opening_index + closing_index) // 2
    inserting_index_left = opening_index
    inserting_index_right = center_index + 1
    inserting_index = opening_index
    while inserting_index_left <= center_index and inserting_index_right <= closing_index:
      if target_elements[inserting_index_left] <= target_elements[inserting_index_right]:
        temporal_elements[inserting_index] = target_elements[inserting_index_left]
        inserting_index +=1
        inserting_index_left += 1
      else:
        temporal_elements[inserting_index] = target_elements[inserting_index_right]
        inserting_index += 1
        inserting_index_right += 1
    while inserting_index_left <= center_index:
      temporal_elements[inserting_index] = target_elements[inserting_index_left]
      inserting_index += 1
      inserting_index_left += 1
    while inserting_index_right <= closing_index:
      temporal_elements[inserting_index] = target_elements[inserting_index_right]
      inserting_index += 1
      inserting_index_right += 1
    for target_index in range(opening_index, closing_index+1):
      target_elements[target_index] = temporal_elements[target_index]
    return


target_elements = [38, 27, 43, 3, 9, 82, 10]
MergeSorter.operate(target_elements)
print(target_elements)