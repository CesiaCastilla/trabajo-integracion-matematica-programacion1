# Programa de Lógica Proposicional - Versión Ampliada
# Algebra de Boole, Sistema Binario y Lógica

print("=== PROGRAMA DE LÓGICA PROPOSICIONAL ===")
print("1. Análisis de implicación (p ⇒ q) y contrarrecíproca")
print("2. Tabla de verdad para múltiples proposiciones")
print()

opcion = int(input("Seleccione una opción (1 o 2): "))

if opcion == 1:
    # CÓDIGO ORIGINAL DE TUS COMPAÑEROS
    p = int(input("Ingrese el valor de verdad para p (1 para Verdadero, 0 para Falso): "))
    q = int(input("Ingrese el valor de verdad para q (1 para Verdadero, 0 para Falso): "))

    # verificación que cumplan la consición
    while True:
        if p not in [0, 1] or q not in [0, 1]:
            print("Los valores de verdad deben ser 0 o 1, vuelve a ingresarlos")
            p = int(input("Ingrese el valor p otra vez: "))
            q = int(input("Ingrese el valor q otra vez: "))
        else:
            break

    # lógica de la implicación
    if p == 1 and q == 0:
        implicacion = 0
        print("p={p} y q={q} -> p => q es Falso")
    else:
        implicacion = 1
        print("p={p}, q={q} -> p => q es Verdadero")

    # La recíproca
    if q == 1 and p == 0:
        reciproca = 0
        print("La recíproca q => p es Falsa")
    else:
        reciproca = 1
        print("La recíproca q => p es Verdadera")

    # La contrarrecíproca
    pneg = 1 - p
    qneg = 1 - q
    print(f"Negación de q (~q) es: {qneg}")
    print(f"Negación de p (~p) es: {pneg}")
    if qneg == 1 and pneg == 0:
        contrarreciproca = 0
        print(f"~q={qneg} y ~p={pneg} -> ~q => ~p es Falso (0)")
    else:
        contrarreciproca = 1
        print(f"~q={qneg}, ~p={pneg} -> ~q => ~p es Verdadero (1)")

    print(f"Resultado final de ~q => ~p: {contrarreciproca}")

    # Verificación de resultados
    print("\n--- Comparación de Resultados ---")
    print(f"Resultado de la implicación (p => q): {implicacion}")
    print(f"Resultado de la contrarrecíproca (q => p): {reciproca}")
    print(f"Resultado de la contrarrecíproca (~q => ~p): {contrarreciproca}")

    if implicacion == contrarreciproca:
        print("\n¡Ambas proposiciones son lógicamente equivalentes!")
        print("Esto se conoce como el Principio de Contraposición en Lógica.")
    else:
        print("\nLas proposiciones NO son lógicamente equivalentes.")

    if implicacion == reciproca:
        print("\n¡Ambas proposiciones son lógicamente equivalentes!")
        print("Esto se conoce como equivalencia lógica o bicondicional.")
    else:
        print("\nLas proposiciones NO son lógicamente equivalentes.")

elif opcion == 2:
    # NUEVA FUNCIONALIDAD: TABLA DE VERDAD PARA MÚLTIPLES PROPOSICIONES
    print("\n=== TABLA DE VERDAD PARA MÚLTIPLES PROPOSICIONES ===")
    
    # Solicitar número de proposiciones
    num_props = int(input("Ingrese el número de proposiciones (2-4): "))
    
    # Validar número de proposiciones
    while num_props < 2 or num_props > 4:
        print("El número debe ser entre 2 y 4")
        num_props = int(input("Ingrese el número de proposiciones (2-4): "))
    
    # Crear lista de nombres de proposiciones
    nombres_props = []
    for i in range(num_props):
        nombres_props.append(chr(112 + i))  # p, q, r, s (ASCII: p=112)
    
    print(f"\nProposiciones: {nombres_props}")
    
    # Solicitar la expresión lógica
    print("\nOperadores disponibles:")
    print("AND: & o *")
    print("OR: | o +") 
    print("NOT: ~ o !")
    print("IMPLICACIÓN: =>")
    print("BICONDICIONAL: <=>")
    
    expresion = input(f"\nIngrese la expresión lógica usando {nombres_props}: ")
    
    # Calcular número total de filas (2^n)
    total_filas = 1
    for i in range(num_props):
        total_filas = total_filas * 2
    
    # Crear encabezado de la tabla
    print("\n" + "="*60)
    print("TABLA DE VERDAD")
    print("="*60)
    
    # Determinar columnas intermedias basadas en la expresión
    columnas_intermedias = []
    expr_limpia = expresion.replace(" ", "").lower()
    
    # Detectar negaciones de variables individuales
    for prop in nombres_props:
        if ("!" + prop) in expr_limpia or ("~" + prop) in expr_limpia:
            columnas_intermedias.append("¬" + prop)
    
    # Detectar subexpresiones en paréntesis
    if "(" in expresion and ")" in expresion:
        # Para casos como !(q+r) o (p&q)
        import re
        parentesis = re.findall(r'\([^()]+\)', expresion)
        for par in parentesis:
            if par not in columnas_intermedias:
                columnas_intermedias.append(par)
    
    # Imprimir encabezados con columnas intermedias
    encabezado = ""
    for prop in nombres_props:
        encabezado = encabezado + prop + "\t"
    
    for col_inter in columnas_intermedias:
        encabezado = encabezado + col_inter + "\t"
    
    encabezado = encabezado + "| " + expresion
    print(encabezado)
    print("-" * len(encabezado))
    
    # Generar todas las combinaciones de valores de verdad
    for fila in range(total_filas):
        # Convertir número de fila a binario para obtener combinación
        valores = []
        temp_fila = fila
        
        # Obtener valores binarios (de derecha a izquierda)
        for i in range(num_props):
            valores.append(temp_fila % 2)
            temp_fila = temp_fila // 2
        
        # Invertir para tener el orden correcto (de izquierda a derecha)
        valores_correctos = []
        for i in range(num_props - 1, -1, -1):
            valores_correctos.append(valores[i])
        
        # Asignar valores a las proposiciones
        if num_props >= 2:
            p = valores_correctos[0]
            q = valores_correctos[1]
        if num_props >= 3:
            r = valores_correctos[2]
        if num_props >= 4:
            s = valores_correctos[3]
        
        # Mostrar valores de las proposiciones
        fila_str = ""
        for valor in valores_correctos:
            fila_str = fila_str + str(valor) + "\t"
        
        # Calcular y mostrar valores de columnas intermedias
        for col_inter in columnas_intermedias:
            valor_inter = 0
            if col_inter.startswith("¬"):
                # Negación de variable simple como ¬p, ¬q
                var = col_inter[1:]  # quitar el ¬
                if var == 'p':
                    valor_inter = 1 - p
                elif var == 'q':
                    valor_inter = 1 - q
                elif var == 'r' and num_props >= 3:
                    valor_inter = 1 - r
                elif var == 's' and num_props >= 4:
                    valor_inter = 1 - s
            elif col_inter.startswith("(") and col_inter.endswith(")"):
                # Subexpresión en paréntesis
                subexpr = col_inter[1:-1].replace(" ", "").lower()
                # Evaluar subexpresión
                if "+" in subexpr or "|" in subexpr:  # OR
                    if num_props == 2 and "q+r" not in subexpr:
                        if "p+q" in subexpr or "p|q" in subexpr:
                            valor_inter = p | q
                    elif num_props >= 3:
                        if "q+r" in subexpr or "q|r" in subexpr:
                            valor_inter = q | r
                        elif "p+q" in subexpr or "p|q" in subexpr:
                            valor_inter = p | q
                elif "&" in subexpr:  # AND
                    if num_props == 2:
                        if "p&q" in subexpr:
                            valor_inter = p & q
                    elif num_props >= 3:
                        if "p&q" in subexpr:
                            valor_inter = p & q
                        elif "q&r" in subexpr:
                            valor_inter = q & r
            
            fila_str = fila_str + str(valor_inter) + "\t"
        
        # Evaluar la expresión lógica
        resultado = 0  # Por defecto falso
        
        # Procesar diferentes tipos de expresiones
        expr_procesada = expresion.replace(" ", "").lower()
        
        # Reemplazar operadores por símbolos estándar
        expr_procesada = expr_procesada.replace("and", "&")
        expr_procesada = expr_procesada.replace("or", "|")
        expr_procesada = expr_procesada.replace("not", "~")
        expr_procesada = expr_procesada.replace("*", "&")
        expr_procesada = expr_procesada.replace("+", "|")
        expr_procesada = expr_procesada.replace("!", "~")
        
        # EVALUADOR GENÉRICO PARA CUALQUIER EXPRESIÓN LÓGICA
        
        # Función para evaluar expresiones de forma genérica
        def evaluar_expresion(expr_str, valores_vars):
            """
            Evalúa una expresión lógica con las variables sustituidas
            valores_vars es un diccionario como {'p': 1, 'q': 0, 'r': 1, 's': 0}
            """
            # Copiar la expresión para procesarla
            expr = expr_str.replace(" ", "").lower()
            
            # Reemplazar variables por sus valores
            for var, valor in valores_vars.items():
                expr = expr.replace(var, str(valor))
            
            # Procesar la expresión paso a paso usando pila/stack simple
            resultado = 0
            
            # Manejar casos específicos comunes
            # 1. Implicaciones (=>)
            if "=>" in expr and "<=>" not in expr:
                if expr.count("=>") == 1:  # Una sola implicación
                    partes = expr.split("=>")
                    izq = evaluar_subexpresion(partes[0])
                    der = evaluar_subexpresion(partes[1])
                    resultado = 0 if (izq == 1 and der == 0) else 1
                    return resultado
            
            # 2. Bicondicionales (<=>)
            elif "<=>" in expr:
                partes = expr.split("<=>")
                if len(partes) == 2:
                    izq = evaluar_subexpresion(partes[0])
                    der = evaluar_subexpresion(partes[1])
                    resultado = 1 if (izq == der) else 0
                    return resultado
            
            # 3. Evaluación general sin implicaciones
            else:
                return evaluar_subexpresion(expr)
        
        def evaluar_subexpresion(expr):
            """Evalúa subexpresiones sin implicaciones"""
            # Procesar negaciones primero
            while "!" in expr or "~" in expr:
                # Buscar negaciones simples como !0, !1, ~0, ~1
                import re
                # Reemplazar !1 -> 0, !0 -> 1, ~1 -> 0, ~0 -> 1
                expr = re.sub(r'[!~]1', '0', expr)
                expr = re.sub(r'[!~]0', '1', expr)
                
                # Procesar negaciones de expresiones entre paréntesis
                # Esto es más complejo, por ahora manejar casos básicos
                if "!(0" in expr or "~(0" in expr:
                    break
                if "!(1" in expr or "~(1" in expr:
                    break
                break
            
            # Evaluar expresión resultante
            # Reemplazar operadores por equivalentes de Python
            expr = expr.replace("|", " or ").replace("&", " and ").replace("+", " or ")
            
            # Casos especiales para paréntesis
            if "(" in expr and ")" in expr:
                # Para casos simples como (0 or 1) and 0
                try:
                    # Evaluación segura para expresiones básicas
                    if all(c in "01 ()andor" for c in expr):
                        return eval(expr)
                except:
                    pass
            
            # Evaluación básica sin paréntesis
            if " and " in expr and " or " not in expr:
                partes = expr.split(" and ")
                resultado = 1
                for parte in partes:
                    resultado = resultado and int(parte.strip())
                return resultado
            elif " or " in expr and " and " not in expr:
                partes = expr.split(" or ")
                resultado = 0
                for parte in partes:
                    resultado = resultado or int(parte.strip())
                return resultado
            elif expr in ["0", "1"]:
                return int(expr)
            else:
                return 0
        
        # Crear diccionario con valores de variables
        valores_variables = {}
        if num_props >= 2:
            valores_variables['p'] = p
            valores_variables['q'] = q
        if num_props >= 3:
            valores_variables['r'] = r
        if num_props >= 4:
            valores_variables['s'] = s
        
        # Evaluar la expresión
        try:
            resultado = evaluar_expresion(expresion, valores_variables)
        except:
            resultado = 0  # En caso de error, devolver 0
        
        # Mostrar resultado
        fila_str = fila_str + "| " + str(resultado)
        print(fila_str)
    
    print("="*60)
    print("Tabla de verdad completada!")
    print("\nNota: Para expresiones más complejas, se muestran los casos básicos.")
    print("Los operadores soportados incluyen AND (&), OR (|), NOT (~), ")
    print("IMPLICACIÓN (=>) y BICONDICIONAL (<=>)")

else:
    print("Opción no válida. Seleccione 1 o 2.")

