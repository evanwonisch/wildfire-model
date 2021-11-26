import numpy as np
from matplotlib import pyplot as plt

class NeighbourState:
    def __init__(self, param_names, param, relative_vector):
        self.param_names = param_names
        self.param = param
        self.relative_vector = relative_vector
        
    def getParam(self, param_name):
        i = self.param_names.index(param_name)
        return self.param[i]
    
    def getRelativeVector(self):
        return self.relativevector

class CellState:
    def __init__(self, param_names, param):
        self.param_names = param_names
        self.param = param
        
    def getParam(self, param_name):
        i = self.param_names.index(param_name)
        return self.param[i]

class ReturnState:
    def __init__(self, param_names, param):
        self.param_names = param_names
        self.param = param
        
    def setParam(self, param_name, value):
        i = self.param_names.index(param_name)
        self.param[i] = value
        
    def addToParam(self,param_name, delta):
        i = self.param_names.index(param_name)
        self.param[i] += delta
        
    def getParam(self, param_name):
        i = self.param_names.index(param_name)
        return self.param[i]

class Grid:
    def __init__(self, rows, cols, param_names, relative_neighbours, transition_function, initial_field_function):
        self.rows = rows
        self.cols = cols
        self.param_names = param_names
        self.n_params = len(param_names)
        self.relative_neighbours = relative_neighbours
        self.transition_function = transition_function
    
        self.field1 = np.zeros(shape = (rows,cols, self.n_params))
        self.field2 = np.zeros(shape = (rows,cols, self.n_params))
        self.active_field = self.field1
        self.inactive_field = self.field2
        
        #read initial field function
        for row in range(rows):
            for col in range(cols):
                initial_values = np.array(initial_field_function(row,col))
                assert initial_values.shape[0] == self.n_params, "initial_field_function does not return the correct number of values" 
                self.active_field[row,col] = initial_values
                    
    def getState(self, row,col):
        return np.copy(self.active_field[row, col])
        
    def getField(self):
        return np.copy(self.active_field)
    
    def getParamField(self, param_name):
        i = self.param_names.index(param_name)
        return np.copy(self.active_field[:,:,i])
    
    def update(self):
        #alle Zellen durchgehen...
        for row in range(self.rows):
            for col in range(self.cols):
                
                #Nachbarinformationen sammeln
                neighbour_states = []
                for relative in self.relative_neighbours:
                    if row + relative[0] in range(self.rows):
                        x = row + relative[0]
                        if col + relative[1] in range(self.cols):
                            y = col + relative[1]
                            
                            #Nachbar existiert
                            neighbour_state = NeighbourState(self.param_names, self.getState(x,y), relative)
                            neighbour_states.append(neighbour_state)
                    
                #Eigene Informationen sammeln
                cell_state = CellState(self.param_names, self.getState(row, col))
                
                #Neuen Satus generieren
                return_state = ReturnState(self.param_names, self.getState(row, col))
                self.transition_function(cell_state, neighbour_states, return_state)
                self.inactive_field[row,col] = return_state.param
        
        #Aktives und Passives Feld vertauschen
        h = self.active_field
        self.active_field = self.inactive_field
        self.inactive_field = h
        
    def runModel(self, n = 1):
        result = np.zeros(shape = (n, self.rows, self.cols, self.n_params))
        
        for i in range(n):
            if i % int(n / 10) == 0:
                print(str(int(100 * (i+1)/n)) + "%")
                
            result[i] = self.getField()
            self.update()
            
        return result