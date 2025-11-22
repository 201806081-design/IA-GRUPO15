# main.py
import argparse
import sys
import os

# Agregar directorio actual al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from train import AutonomousDrivingTrainer
from test import AutonomousDrivingTester
from config import PATHS

def main():
    parser = argparse.ArgumentParser(description='Sistema de Conducción Autónoma - UMSS')
    parser.add_argument('--mode', type=str, choices=['train', 'test', 'demo'], 
                       default='train', help='Modo de ejecución')
    parser.add_argument('--episodes', type=int, default=500, 
                       help='Número de episodios para entrenamiento')
    parser.add_argument('--model', type=str, 
                       default=f"{PATHS['models']}autonomous_driver_final.pth",
                       help='Ruta del modelo para prueba/demo')
    
    args = parser.parse_args()
    
    print("🚗 SISTEMA DE CONDUCCIÓN AUTÓNOMA")
    print("📚 Universidad Mayor de San Simón")
    print("🏫 Facultad de Ciencias y Tecnología")
    print("👥 Integrantes:")
    print("   - Barrios Muni Jhessica")
    print("   - Bejarano Soria Nicolas Santiago") 
    print("   - Padilla Luizaga Carlos Randal")
    print("📖 Materia: Inteligencia Artificial I")
    print("🔬 Área: Aprendizaje por Refuerzo")
    print("👁️  Subárea: Visión por Computadora")
    print("="*50)
    
    if args.mode == 'train':
        print("🎯 MODO: ENTRENAMIENTO")
        trainer = AutonomousDrivingTrainer()
        trainer.train(num_episodes=args.episodes)
        
    elif args.mode == 'test':
        print("🧪 MODO: PRUEBA")
        tester = AutonomousDrivingTester(args.model)
        tester.test(num_episodes=5, render=True)
        
    elif args.mode == 'demo':
        print("🎮 MODO: DEMOSTRACIÓN")
        tester = AutonomousDrivingTester(args.model)
        tester.test(num_episodes=3, render=True)

if __name__ == "__main__":
    main()