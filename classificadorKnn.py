class Classificador:
    '''
    Métodos: distance_verifier, find_closer_points, class_def, class_all_points, print_points
    '''
    def __init__(self, data, no_class, k):
        '''Atributo 'data': Lista com investidores já classificados
        Atributo 'no_class': Lista com investidores não classificados
        Atributo 'k': Valor K do algorítimo K-NN
        '''
        self.data = data
        self.no_class = no_class
        self.k = k
    
    def distance_verifier(self, p_data, p_no_class):
        '''Verifique a distância entre 2 pontos
        Atributo 'p_data': tupla com valores do investidor classificado
        Atributo 'p_no_class': tupla com valores do investidor não classificado
        Retorna a distância
        '''
        d = 0
        for i in range(len(p_data)):
            d += (p_data[i] - p_no_class[i]) ** 2
        d = d ** (1 / 2)
        return d
    
    def find_closer_points(self, i): # Função para encontrar os pontos mais próximos
        '''Encontre pontos mais próximos do ponto a ser classificado
        Atributo 'i': range para o loop for
        Retorna uma lista com os pontos mais próximos'''
        data_distances = []
        closer_distances = []
        closer_points = []
    
        # Para cada ponto na lista 'data', verifique a distancia entre os valores
        # do ponto [i]  e os valores do ponto
        for point in self.data:
            data_distances.append(self.distance_verifier(self.no_class[i][2], point[2]))

        data_distances = list(enumerate(data_distances))
        data_distances.sort(key=lambda elem: elem[1])
        closer_distances = data_distances[:self.k]

        for element in closer_distances:
            closer_points.append(element[0])
        return closer_points
    
    def class_def(self, closer_points): # Função para definir a classe do ponto baseado nos pontos mais próximos
        '''Define a classe de um ponto
        Atributo 'closer_points': Lista com os pontos mais próximos do ponto a ser definido
        Retorna uma string com a classe do ponto'''
        closer_points_class = []
        c_con = 0
        c_mod = 0
        c_agr = 0
        for i in closer_points:
            closer_points_class.append(self.data[i][1])
        c_con = closer_points_class.count('Conservador')
        c_mod = closer_points_class.count('Moderado')
        c_agr = closer_points_class.count('Agressivo')
        if c_con > c_mod and c_con > c_agr:
            p_class = 'Conservador'
        elif c_mod > c_con and c_mod > c_agr:
            p_class = 'Moderado'
        elif c_agr > c_con and c_agr > c_mod:
            p_class = 'Agressivo'
        else:
            p_class = 'Não definido'
        return p_class
    
    def class_all_points(self):
        '''Classifica todos os pontos
        Retorna um dicionário com os CPF's como chave e a classificação como valor'''
        points_classified = {}
        for i in range(len(self.no_class)):
            cl_points = self.find_closer_points(i)
            p_class = self.class_def(cl_points)
            points_classified[self.no_class[i][0]] = p_class
        return points_classified
    
    def print_points(self, points_classified):
        '''Imprime todos os pontos
        Atributo 'points_classified': dicionário com os cpfs e as classificações'''
        for key in points_classified:
            print(key, ':', points_classified[key])