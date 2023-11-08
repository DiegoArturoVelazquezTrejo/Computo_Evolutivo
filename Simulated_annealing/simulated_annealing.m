% Implementación del recocido simulado a un problema de optimización 

% @param: F (función objetivo)
% @param: Fs (función de vecindad)
% @param: T (temperatura inicial)
% @param: I0 (estado inicial del algoritmo; x0 )
% @param: IT0 (cota inferior para la temperatura)
% @param: E (regla con la que decrecemos la temperatura)
% @param: I (número de iteraciones máximo)

function [act, val_min] = simulatedAnnealing(F, Fs, T, I0, IT0, E, I)

    act = I0; % Nos posicionamos en el estado inicial 
    iteracion = 1; 
    
    val_min = act; % Valor mínimo de la función objetivo
    F_val_min = F(act); % Valor mínimo evaluado en la función objetivo
    
    while(T > IT0 || iteracion < I)
    
        % Generamos un estado vecino
        vecino = Fs(act);
    
        % Vamos a realizar el cálculo de las funciones una vez por iteración 
        f_vecino = F(vecino); 
        f_act = F(act); 
        
        % Calculamos la diferencia de la función objetivo entre el estado actual y el vecino
        delta = f_vecino - f_act;
        
        % Si el vecino es mejor que el estado actual, nos movemos a él
        if(delta < 0)
            act = vecino;
        else
            % Si el vecino es peor que el estado actual, nos movemos a él con una probabilidad
            % que depende de la temperatura y de la diferencia de la función objetivo
            if(rand() < exp(-delta/T))
                act = vecino;
            end
        end
        % Actualización del óptimo global encontrado por el algoritmo 
        if(f_act < F_val_min)
            val_min = act;
            F_val_min = f_act;
        end
        
        % Actualizamos la temperatura
        T = E(T);
        
        % Actualizamos el número de iteraciones
        iteracion = iteracion + 1;
    end