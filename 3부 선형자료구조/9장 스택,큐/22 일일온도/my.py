class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
      result = []

      for index, item in enumerate(temperatures):
          count = 0
          cursor = index
      
          while True :
              if cursor + 1 >= len(temperatures):
                  result.append(0)
                  break
      
              if item >= temperatures[cursor + 1]:
                  cursor += 1
                  count += 1
              else:
                  count += 1
                  result.append(count)
                  break
              
      return result

      #타임 리미트