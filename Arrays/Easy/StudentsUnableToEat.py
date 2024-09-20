# Solution with O(1) memory, O(n+k) time (where k is how many times we need to re-arrange the students)
class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        unable = 0
        while students:
            curr_student = students.pop(0)
            curr_sandwich = sandwiches[0]
            if curr_student == curr_sandwich:
                sandwiches.pop(0)
                unable=0
            else:
                unable+=1
                students.append(curr_student)
            if unable==len(students):
                break
                
        return len(sandwiches)

# Solution with O(n) time & memory
class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        unable_to_eat = len(students)
        students_dict = Counter(students)
        for s in sandwiches:
            if students_dict[s]>0:
                students_dict[s]-=1
                unable_to_eat-=1
            else:
                return unable_to_eat        
        
        return unable_to_eat