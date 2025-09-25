print("1. Análisis de implicación (p ⇒ q) y contrarrecíproca")
print("2. Tabla de verdad para múltiples proposiciones")
print()

opcion = int(input("Seleccione una opción (1 o 2): "))

if opcion == 1:
    # CÓDIGO ORIGINAL DE LOS COMPAÑEROS
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
    
    # Imprimir encabezados
    encabezado = ""
    for prop in nombres_props:
        encabezado = encabezado + prop + "\t"
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
        
        # Evaluar expresiones comunes paso a paso
        if num_props == 2:
            # Reemplazar variables por sus valores
            expr_eval = expr_procesada
            expr_eval = expr_eval.replace("p", str(p))
            expr_eval = expr_eval.replace("q", str(q))
            
            # Evaluar diferentes tipos de expresiones
            if "<=>" in expr_eval:  # Bicondicional
                partes = expr_eval.split("<=>")
                if len(partes) == 2:
                    lado_izq = partes[0].strip()
                    lado_der = partes[1].strip()
                    if lado_izq == lado_der:
                        resultado = 1
                    else:
                        resultado = 0
            elif "=>" in expr_eval:  # Implicación
                partes = expr_eval.split("=>")
                if len(partes) == 2:
                    lado_izq = int(partes[0].strip())
                    lado_der = int(partes[1].strip())
                    if lado_izq == 1 and lado_der == 0:
                        resultado = 0
                    else:
                        resultado = 1
            elif "&" in expr_eval and "|" not in expr_eval:  # Solo AND
                if "~" in expr_eval:
                    if "~" + str(p) in expr_eval and str(q) in expr_eval:
                        resultado = (1-p) & q
                    elif str(p) in expr_eval and "~" + str(q) in expr_eval:
                        resultado = p & (1-q)
                    elif "~" + str(p) in expr_eval and "~" + str(q) in expr_eval:
                        resultado = (1-p) & (1-q)
                else:
                    resultado = p & q
            elif "|" in expr_eval and "&" not in expr_eval:  # Solo OR
                if "~" in expr_eval:
                    if "~" + str(p) in expr_eval and str(q) in expr_eval:
                        resultado = (1-p) | q
                    elif str(p) in expr_eval and "~" + str(q) in expr_eval:
                        resultado = p | (1-q)
                    elif "~" + str(p) in expr_eval and "~" + str(q) in expr_eval:
                        resultado = (1-p) | (1-q)
                else:
                    resultado = p | q
            elif "~" in expr_eval and "&" not in expr_eval and "|" not in expr_eval:  # Solo NOT
                if "~p" in expr_eval and "q" not in expr_eval:
                    resultado = 1 - p
                elif "~q" in expr_eval and "p" not in expr_eval:
                    resultado = 1 - q
        
        elif num_props == 3:
            # Para 3 proposiciones
            expr_eval = expr_procesada
            expr_eval = expr_eval.replace("p", str(p))
            expr_eval = expr_eval.replace("q", str(q))
            expr_eval = expr_eval.replace("r", str(r))
            
            # Evaluar expresiones simples con 3 variables
            if "&" in expr_eval and "|" not in expr_eval:
                # p & q & r
                resultado = p & q & r
            elif "|" in expr_eval and "&" not in expr_eval:
                # p | q | r
                resultado = p | q | r
            elif "&" in expr_eval and "|" in expr_eval:
                # Expresiones mixtas como (p & q) | r
                if "(p&q)|r" in expr_eval.replace(" ", ""):
                    resultado = (p & q) | r
                elif "p&(q|r)" in expr_eval.replace(" ", ""):
                    resultado = p & (q | r)
                elif "(p|q)&r" in expr_eval.replace(" ", ""):
                    resultado = (p | q) & r
                elif "p|(q&r)" in expr_eval.replace(" ", ""):
                    resultado = p | (q & r)
        
        elif num_props == 4:
            # Para 4 proposiciones (casos básicos)
            expr_eval = expr_procesada
            expr_eval = expr_eval.replace("p", str(p))
            expr_eval = expr_eval.replace("q", str(q))
            expr_eval = expr_eval.replace("r", str(r))
            expr_eval = expr_eval.replace("s", str(s))
            
            if "&" in expr_eval and "|" not in expr_eval:
                resultado = p & q & r & s
            elif "|" in expr_eval and "&" not in expr_eval:
                resultado = p | q | r | s
        
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


