# from fractions import Fraction

# class Check:
#     def __init__(self, coordinates):
#         assert all(isinstance(p, tuple) and len(p) == 2 for p in coordinates), "Error: All points in coordinates must be tuples of length 2"
#         self.coordinates = coordinates
#         self.points = coordinates + [coordinates[0]]
        

#     def firs_equation(self, p1, p2):
#         temp = Fraction((p2[1]-p1[1])/(p2[0]-p1[0])).limit_denominator()
#         a = temp
#         temp1 = Fraction(temp*p1[0]).limit_denominator()
#         b = Fraction(p1[1] - temp1).limit_denominator()
#         return a, b
    
#     def calculate_area_triangle(self, p):
#         p1, p2, p3 = p
#         area = abs(1/2 * (p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1])))
#         return area
    
#     def check_in_edge(self, p: tuple):
#         def check_position(p, p1, p2):
#             if (p1[0] <= p[0] <= p2[0] or p2[0] <= p[0] <= p1[0]) and (p1[1] <= p[1] <= p2[1] or p2[1] <= p[1] <= p1[1]):
#                 return True
#             return False
        
#         edges = ['AB', 'BC', 'CA']
#         for i in range(len(self.points)-1):
#             a, b = self.firs_equation(self.points[i], self.points[i+1])
#             print(a,b)
#             if p[1] == a*p[0] + b and check_position(p, self.points[i], self.points[i+1]) :
#                 return 'This point is in {} edge of triangle'.format(edges[i])
            
#         return False
    
#     def check_in_triangle(self, p: tuple):
#         print(self.coordinates)
#         area_ABC = self.calculate_area_triangle(self.coordinates)
#         sum_of_area = 0
#         if not self.check_in_edge(p):
#             for i in range(len(self.points)-1):
#                 area = self.calculate_area_triangle([self.points[i], self.points[i+1], p])
#                 sum_of_area += area
        
#         if sum_of_area == area_ABC:
#             return 'This point is in triangle'
#         return False
    
# A = (6, 4)
# B = (3, 2)
# C = (8, 3)
# p = (7, 3)

# check = Check([A, B, C])
# print(check.check_in_triangle((p)))

print(len("m************"))