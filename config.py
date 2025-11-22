
import os

# Configuración de CARLA
CARLA_PATH = "C:/CARLA_0.9.14/WindowsNoEditor"  # Ajustar según tu instalación
CARLA_HOST = 'localhost'
CARLA_PORT = 2000
CARLA_TIMEOUT = 20.0

# Configuración del modelo DQN
MODEL_CONFIG = {
    'state_size': 512,  # Tamaño del estado basado en características de la CNN
    'action_size': 5,   # Acelerar, Frenar, Izquierda, Derecha, Mantener
    'hidden_size': 256,
    'learning_rate': 0.001,
    'gamma': 0.99,
    'epsilon_start': 1.0,
    'epsilon_end': 0.01,
    'epsilon_decay': 0.995,
    'memory_size': 10000,
    'batch_size': 32,
    'update_target_every': 1000
}

# Configuración de recompensas
REWARD_CONFIG = {
    'center_lane': 0.1,
    'off_center': -0.1,
    'speed_optimal': 0.05,
    'speed_too_slow': -0.02,
    'speed_too_fast': -0.1,
    'collision': -10.0,
    'traffic_light_green': 0.0,
    'traffic_light_red_penalty': -2.0,
    'traffic_light_red_reward': 0.5,
    'progress': 0.2,
    'object_detected': -0.5,
    'safe_distance': 0.05
}

# Configuración de sensores
SENSOR_CONFIG = {
    'camera': {
        'width': 640,
        'height': 480,
        'fov': 90
    },
    'lidar': {
        'channels': 32,
        'range': 50,
        'points_per_second': 100000
    }
}

# Configuración de entrenamiento
TRAINING_CONFIG = {
    'max_episode_steps': 1000,
    'target_success_rate': 0.7,
    'save_model_every': 100,
    'render_every': 50
}

# Rutas de archivos
PATHS = {
    'models': 'models/',
    'logs': 'logs/',
    'data': 'data/'
}

for path in PATHS.values():
    os.makedirs(path, exist_ok=True)