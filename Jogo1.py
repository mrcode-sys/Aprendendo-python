from ursina import *

class CarP(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed = 5  # Velocidade de movimento
        self.collider = 'box' # Define um colisor para a entidade

    def update(self):
        # Move o carro com as setas ou WASD
        if held_keys['a'] or held_keys['left arrow']:
            self.x -= time.dt * self.speed
        if held_keys['d'] or held_keys['right arrow']:
            self.x += time.dt * self.speed
        if held_keys['w'] or held_keys['up arrow']:
            self.z += time.dt * self.speed
        if held_keys['s'] or held_keys['down arrow']:
            self.z -= time.dt * self.speed
# Continuação do arquivo meu_jogo.py
app = Ursina()

# Adiciona o carro
carP = CarP(
    model='cube',
    color=color.blue,
    scale=0.5,
    position=(0, 0, 0)
)

# Adiciona a câmera que segue o carro
camera.parent = carP
camera.position = (0, 2, -10) # Posição da câmera em relação ao carro
camera.rotation = (4,0,0)

# Adiciona um chão
ground = Entity(
    model='plane',
    scale=(100, 1, 100),
    color=color.gray,
    texture='white_cube',
    collider='box',
    position=(0, -1, 0)
)

# Inicia o jogo
app.run()