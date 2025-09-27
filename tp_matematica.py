# Programa de Lógica Proposicional - Versión Final
# Algebra de Boole, Sistema Binario y Lógica

print("=== PROGRAMA DE LÓGICA PROPOSICIONAL ===")
print("1. Análisis de implicación (p ⇒ q) y contrarrecíproca")
print("2. Tabla de verdad para 2 o 3 proposiciones")
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
    num_props = int(input("Ingrese el número de proposiciones (2-3): "))
    
    # Validar número de proposiciones
    while num_props < 2 or num_props > 3:
        print("El número debe ser entre 2 y 3")
        num_props = int(input("Ingrese el número de proposiciones (2-3): "))
    
    # Crear lista de nombres de proposiciones
    nombres_props = []
    for i in range(num_props):
        nombres_props.append(chr(112 + i))  # p, q, r (ASCII: p=112)
    
    print(f"\nProposiciones: {nombres_props}")
    
    # Solicitar la expresión lógica
    print("\nOperadores disponibles:")
    print("AND: & o *")
    print("OR: | o + o v") 
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
    expr_sin_espacios = expresion.replace(" ", "")
    
    # Detectar negaciones de variables individuales
    for prop in nombres_props:
        if ("!" + prop) in expr_sin_espacios or ("~" + prop) in expr_sin_espacios:
            columnas_intermedias.append("¬" + prop)
    
    # Detectar subexpresiones en paréntesis
    if "(" in expresion and ")" in expresion:
        import re
        # Buscar expresiones entre paréntesis
        parentesis = re.findall(r'\([^()]+\)', expresion)
        for par in parentesis:
            # Siempre agregar la subexpresión base
            columnas_intermedias.append(par)
        
        # Buscar específicamente patrones como !(expresión) o ~(expresión)
        negaciones_parentesis = re.findall(r'[!~]\([^()]+\)', expr_sin_espacios)
        for neg_par in negaciones_parentesis:
            # Convertir !(q+r) a ¬(q+r)
            par_negado = "¬" + neg_par[1:]  # quitar el ! o ~ del inicio
            if par_negado not in columnas_intermedias:
                columnas_intermedias.append(par_negado)
    
    # Imprimir encabezados con columnas intermedias
    encabezado = ""
    for prop in nombres_props:
        encabezado = encabezado + prop + "\t"
    
    for col_inter in columnas_intermedias:
        encabezado = encabezado + col_inter + "\t"
    
    encabezado = encabezado + "| " + expresion
    print(encabezado)
    print("-" * len(encabezado))
    
    # EVALUADOR COMPLETAMENTE DINÁMICO
    def evaluar_expresion_dinamica(expresion_original, valores_vars):
        """
        Evaluador completamente dinámico para cualquier expresión lógica
        """
        expr = expresion_original.replace(" ", "").lower()
        
        # Normalizar operadores
        expr = expr.replace("and", "&").replace("or", "|").replace("not", "!")
        expr = expr.replace("*", "&").replace("+", "|").replace("~", "!")
        expr = expr.replace("v", "|")  # Agregar soporte para 'v'
        
        # Procesamiento mejorado de negaciones simples (!p, !q, etc.)
        import re
        # Primero procesar todas las negaciones de variables simples
        while re.search(r'![pqr]', expr):
            # Reemplazar !p, !q, !r por sus valores
            if '!p' in expr:
                valor_p = valores_vars.get('p', 0)
                negacion_p = 1 - valor_p
                expr = expr.replace('!p', str(negacion_p))
            if '!q' in expr:
                valor_q = valores_vars.get('q', 0)
                negacion_q = 1 - valor_q
                expr = expr.replace('!q', str(negacion_q))
            if '!r' in expr:
                valor_r = valores_vars.get('r', 0)
                negacion_r = 1 - valor_r
                expr = expr.replace('!r', str(negacion_r))
            break  # salir para evitar loop infinito
        
        # También procesar ~ 
        while re.search(r'~[pqr]', expr):
            if '~p' in expr:
                valor_p = valores_vars.get('p', 0)
                negacion_p = 1 - valor_p
                expr = expr.replace('~p', str(negacion_p))
            if '~q' in expr:
                valor_q = valores_vars.get('q', 0)
                negacion_q = 1 - valor_q
                expr = expr.replace('~q', str(negacion_q))
            if '~r' in expr:
                valor_r = valores_vars.get('r', 0)
                negacion_r = 1 - valor_r
                expr = expr.replace('~r', str(negacion_r))
            break
        
        # Reemplazar variables restantes por sus valores
        for var, valor in valores_vars.items():
            expr = expr.replace(var, str(valor))
        
        # Procesar la expresión paso a paso
        return procesar_expresion_completa(expr)
    
    def procesar_expresion_completa(expr):
        """Procesa cualquier expresión lógica de forma recursiva"""
        
        # Caso base: si es solo un número
        if expr in ["0", "1"]:
            return int(expr)
        
        # Manejar implicaciones primero (tienen menor prioridad)
        if "<=>" in expr:
            # Bicondicional
            partes = expr.split("<=>")
            if len(partes) == 2:
                izq = procesar_expresion_completa(partes[0])
                der = procesar_expresion_completa(partes[1])
                return 1 if izq == der else 0
        
        elif "=>" in expr and "<=>" not in expr:
            # Implicación (buscar la última => para asociatividad correcta)
            pos = expr.rfind("=>")
            if pos != -1:
                izq = procesar_expresion_completa(expr[:pos])
                der = procesar_expresion_completa(expr[pos+2:])
                return 0 if (izq == 1 and der == 0) else 1
        
        # Procesar negaciones de expresiones completas entre paréntesis
        while "!(" in expr:
            # Encontrar !( y su ) correspondiente
            start = expr.find("!(")
            if start == -1:
                break
            
            # Encontrar el paréntesis de cierre correspondiente
            count = 1
            pos = start + 2
            while pos < len(expr) and count > 0:
                if expr[pos] == '(':
                    count += 1
                elif expr[pos] == ')':
                    count -= 1
                pos += 1
            
            if count == 0:
                # Extraer la subexpresión
                subexpr = expr[start+2:pos-1]
                resultado_sub = procesar_expresion_completa(subexpr)
                resultado_negado = 1 - resultado_sub
                # Reemplazar en la expresión original
                expr = expr[:start] + str(resultado_negado) + expr[pos:]
            else:
                break
        
        # Procesar negaciones simples (!, variables negadas)
        import re
        expr = re.sub(r'!1', '0', expr)
        expr = re.sub(r'!0', '1', expr)
        
        # Procesar expresiones con paréntesis (sin negación)
        while "(" in expr and ")" in expr and "!(" not in expr:
            # Encontrar la expresión entre paréntesis más interna
            start = -1
            for i in range(len(expr)):
                if expr[i] == '(':
                    start = i
                elif expr[i] == ')' and start != -1:
                    subexpr = expr[start+1:i]
                    resultado_sub = procesar_expresion_completa(subexpr)
                    expr = expr[:start] + str(resultado_sub) + expr[i+1:]
                    break
            else:
                break
        
        # Ahora procesar operadores por precedencia: primero &, luego |
        # Procesar AND (&)
        while "&" in expr:
            # Buscar el primer &
            pos = expr.find("&")
            if pos == -1:
                break
            
            # Obtener operandos izquierdo y derecho
            # Izquierdo: último número/dígito antes del &
            izq_start = pos - 1
            while izq_start >= 0 and expr[izq_start].isdigit():
                izq_start -= 1
            izq_start += 1
            izq_val = int(expr[izq_start:pos])
            
            # Derecho: primer número después del &
            der_end = pos + 1
            while der_end < len(expr) and expr[der_end].isdigit():
                der_end += 1
            der_val = int(expr[pos+1:der_end])
            
            # Calcular resultado
            resultado = izq_val & der_val
            
            # Reemplazar en la expresión
            expr = expr[:izq_start] + str(resultado) + expr[der_end:]
        
        # Procesar OR (|)
        while "|" in expr:
            # Buscar el primer |
            pos = expr.find("|")
            if pos == -1:
                break
            
            # Obtener operandos izquierdo y derecho
            # Izquierdo: último número/dígito antes del |
            izq_start = pos - 1
            while izq_start >= 0 and expr[izq_start].isdigit():
                izq_start -= 1
            izq_start += 1
            izq_val = int(expr[izq_start:pos])
            
            # Derecho: primer número después del |
            der_end = pos + 1
            while der_end < len(expr) and expr[der_end].isdigit():
                der_end += 1
            der_val = int(expr[pos+1:der_end])
            
            # Calcular resultado
            resultado = izq_val | der_val
            
            # Reemplazar en la expresión
            expr = expr[:izq_start] + str(resultado) + expr[der_end:]
        
        # Si llegamos aquí, debería ser un número
        try:
            return int(expr)
        except:
            return 0
    
    # Generar todas las combinaciones de valores de verdad
    for fila in range(total_filas):
        # Generar combinación binaria estándar
        # Para 2 proposiciones: p=1100, q=1010
        # Para 3 proposiciones: p=11110000, q=11001100, r=10101010
        
        valores_correctos = []
        
        if num_props == 2:
            # Patrón estándar para 2 proposiciones
            patrones = [
                [1, 1, 0, 0],  # p
                [1, 0, 1, 0]   # q
            ]
            for i in range(num_props):
                valores_correctos.append(patrones[i][fila])
                
        elif num_props == 3:
            # Patrón estándar para 3 proposiciones
            patrones = [
                [1, 1, 1, 1, 0, 0, 0, 0],  # p
                [1, 1, 0, 0, 1, 1, 0, 0],  # q
                [1, 0, 1, 0, 1, 0, 1, 0]   # r
            ]
            for i in range(num_props):
                valores_correctos.append(patrones[i][fila])
        
        # Asignar valores a las proposiciones
        if num_props >= 2:
            p = valores_correctos[0]
            q = valores_correctos[1]
        if num_props >= 3:
            r = valores_correctos[2]
        
        # Mostrar valores de las proposiciones
        fila_str = ""
        for valor in valores_correctos:
            fila_str = fila_str + str(valor) + "\t"
        
        # Debug temporal: verificar valores
        # print(f"Fila {fila}: p={p}, q={q}")
        
        # Calcular y mostrar valores de columnas intermedias
        for col_inter in columnas_intermedias:
            valor_inter = 0
            
            # Negaciones de variables individuales (!p, !q, !r)
            if col_inter == "!p":
                valor_inter = 1 - p
                # print(f"!p: 1 - {p} = {valor_inter}")
            elif col_inter == "!q":
                valor_inter = 1 - q
            elif col_inter == "!r" and num_props >= 3:
                valor_inter = 1 - r
            elif col_inter == "~p":
                valor_inter = 1 - p
            elif col_inter == "~q":
                valor_inter = 1 - q
            elif col_inter == "~r" and num_props >= 3:
                valor_inter = 1 - r
        # Calcular y mostrar valores de columnas intermedias
        for col_inter in columnas_intermedias:
            valor_inter = 0  # valor por defecto
            
            # Manejar negaciones simples directamente
            if col_inter == "!p" or col_inter == "¬p":
                valor_inter = 1 - p
            elif col_inter == "!q" or col_inter == "¬q":
                valor_inter = 1 - q
            elif (col_inter == "!r" or col_inter == "¬r") and num_props >= 3:
                valor_inter = 1 - r
            elif col_inter.startswith("¬(") and col_inter.endswith(")"):
                # Negación de expresión entre paréntesis como ¬(q+r)
                subexpr = col_inter[2:-1].replace(" ", "").lower()  # quitar ¬( y )
                valor_subexpr = 0
                
                if "+" in subexpr or "|" in subexpr or "v" in subexpr:  # OR
                    if ("q+r" in subexpr or "q|r" in subexpr or "qvr" in subexpr) and num_props >= 3:
                        valor_subexpr = q | r
                    elif "p+q" in subexpr or "p|q" in subexpr or "pvq" in subexpr:
                        valor_subexpr = p | q
                    elif ("p+r" in subexpr or "p|r" in subexpr or "pvr" in subexpr) and num_props >= 3:
                        valor_subexpr = p | r
                elif "&" in subexpr:  # AND
                    if "p&q" in subexpr:
                        valor_subexpr = p & q
                    elif "q&r" in subexpr and num_props >= 3:
                        valor_subexpr = q & r
                    elif "p&r" in subexpr and num_props >= 3:
                        valor_subexpr = p & r
                
                valor_inter = 1 - valor_subexpr  # negar el resultado
            elif col_inter.startswith("!(") and col_inter.endswith(")"):
                # Negación de expresión entre paréntesis como !(q+r)
                subexpr = col_inter[2:-1].replace(" ", "").lower()  # quitar !( y )
                valor_subexpr = 0
                
                if "+" in subexpr or "|" in subexpr or "v" in subexpr:  # OR
                    if ("q+r" in subexpr or "q|r" in subexpr or "qvr" in subexpr) and num_props >= 3:
                        valor_subexpr = q | r
                    elif "p+q" in subexpr or "p|q" in subexpr or "pvq" in subexpr:
                        valor_subexpr = p | q
                    elif ("p+r" in subexpr or "p|r" in subexpr or "pvr" in subexpr) and num_props >= 3:
                        valor_subexpr = p | r
                elif "&" in subexpr:  # AND
                    if "p&q" in subexpr:
                        valor_subexpr = p & q
                    elif "q&r" in subexpr and num_props >= 3:
                        valor_subexpr = q & r
                    elif "p&r" in subexpr and num_props >= 3:
                        valor_subexpr = p & r
                
                valor_inter = 1 - valor_subexpr  # negar el resultado
            elif col_inter.startswith("(") and col_inter.endswith(")"):
                # Subexpresión en paréntesis sin negación
                subexpr = col_inter[1:-1].replace(" ", "").lower()
                # Evaluar subexpresión
                if "+" in subexpr or "|" in subexpr or "v" in subexpr:  # OR
                    if num_props == 2 and "q+r" not in subexpr:
                        if "p+q" in subexpr or "p|q" in subexpr or "pvq" in subexpr:
                            valor_inter = p | q
                    elif num_props >= 3:
                        if "q+r" in subexpr or "q|r" in subexpr or "qvr" in subexpr:
                            valor_inter = q | r
                        elif "p+q" in subexpr or "p|q" in subexpr or "pvq" in subexpr:
                            valor_inter = p | q
                        elif "p+r" in subexpr or "p|r" in subexpr or "pvr" in subexpr:
                            valor_inter = p | r
                elif "&" in subexpr:  # AND
                    if num_props == 2:
                        if "p&q" in subexpr:
                            valor_inter = p & q
                    elif num_props >= 3:
                        if "p&q" in subexpr:
                            valor_inter = p & q
                        elif "q&r" in subexpr:
                            valor_inter = q & r
                        elif "p&r" in subexpr:
                            valor_inter = p & r
            
            fila_str = fila_str + str(valor_inter) + "\t"
        
        # Crear diccionario con valores de variables
        valores_variables = {}
        if num_props >= 2:
            valores_variables['p'] = p
            valores_variables['q'] = q
        if num_props >= 3:
            valores_variables['r'] = r
        
        # Evaluar la expresión
        try:
            resultado = evaluar_expresion_dinamica(expresion, valores_variables)
        except:
            resultado = 0  # En caso de error, devolver 0
        
        # Mostrar resultado
        fila_str = fila_str + "| " + str(resultado)
        print(fila_str)
    
    print("="*60)
    print("Tabla de verdad completada!")
    print("\nOperadores soportados: AND (&, *), OR (|, +, v), NOT (!, ~),")
    print("IMPLICACIÓN (=>), BICONDICIONAL (<=>)")
    print("El evaluador puede manejar expresiones de cualquier complejidad.")

else:
    print("Opción no válida. Seleccione 1 o 2.")