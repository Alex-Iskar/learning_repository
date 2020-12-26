# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__())
class Matrix:
    def __init__(self, m_l):
        self.mt = m_l
        self.rows = len(m_l)
        if type(self.mt[0]) == list:
            self.n_cols = len(self.mt[0])
        else:
            self.n_cols = 0

    def __str__(self):
        if self.n_cols > 0:
            str_mt = "{}\n" * self.rows
            return str_mt.format(*self.mt)
        else:
            return f"{self.mt}"

    def __add__(self, other):
        result = []
        for i in range(0, self.rows):
            if self.n_cols > 0:
                line = []
                for j in range(0, self.n_cols):
                    line.append(self.mt[i][j] + other.mt[i][j])
                result.append(line)
            else:
                result.append(self.mt[i] + other.mt[i])
        return Matrix(result)


s_m_1 = Matrix([[1, 2, 3], [1, 2, 3]])
s_m_2 = Matrix([[9, 9, 9], [9, 9, 9]])
s_m_3 = Matrix([[9, 9, 9], [9, 9, 9]])
print(s_m_1)
print(s_m_1 + s_m_2 + s_m_3)