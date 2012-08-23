import os.path
from datetime import datetime

class Kifu:
    """Create file(.sgf) for save the game. """

    def __init__(self, player_black="black", player_white="white", handicap=0, path="sgf"):
        """ Add information about players, path, filename. """
        self.num_jug = 0
        self.player_black = player_black
        self.player_white = player_white
                
        filename = str(datetime.now())  + "_" + player_black + "_" + player_white

        f = open("%s/%s.sgf" %(self.path, filename), "w") 
        for elem in cte.INITSGF:
            f.write(elem)
        f.close()    

    def add_stone(self, pos, color):
        pass

    def add_stones(pos_list, color_list):# add problem or state
        pass

    def __str__():
        pass

    def __init__(self, path = "sgf"):
        num = 0
        self.path = path
        self.cadena = cte.PLAYER_B + "-" + cte.PLAYER_W
        name = self.cadena
        try: 
            while 1:
                file = open("%s/%s.sgf" %(self.path, self.cadena), "r") # TODO existe el archivo
                file.close()
                num += 1                
                self.cadena = name + "(" + str(num) + ")"
        except IOError:
            file = open("%s/%s.sgf" %(self.path, self.cadena), "w")
            for elem in cte.INITSGF:
                file.write(elem)
            file.close()    
            
    def add_text(self, text, color):
        file = open("%s/%s.sgf" %(self.path, self.cadena), "a")
        if color == cte.BLACK:
            file.write("\n;B[%s]" %text)
        elif color == cte.WHITE:
            file.write("\n;W[%s]" %text)
        else:
            print _("el color debe ser BLACK or WHITE")
        file.close()
        
    def end_file(self):
        file = open("%s/%s.sgf" %(self.path, self.cadena), "a")
        file.write("))")
        file.close()


