class Node {
    constructor(dato) {
      this.dato = dato;
      this.izq = null;
      this.der = null;
    }
  }
  
  // a) Inorden: Izquierda - Raíz - Derecha
  function inordenIterativo(raiz) {
    let stack = [];
    let actual = raiz;
    while (stack.length > 0 || actual !== null) {
      while (actual !== null) {
        stack.push(actual);
        actual = actual.izq;
      }
      actual = stack.pop();
      console.log(actual.dato);
      actual = actual.der;
    }
  }
  
  // b) Postorden: Izquierda - Derecha - Raíz
  function postordenIterativo(raiz) {
    if (!raiz) return;
    let stack1 = [raiz];
    let stack2 = [];
    while (stack1.length > 0) {
      let nodo = stack1.pop();
      stack2.push(nodo);
      if (nodo.izq) stack1.push(nodo.izq);
      if (nodo.der) stack1.push(nodo.der);
    }
    while (stack2.length > 0) {
      console.log(stack2.pop().dato);
    }
  }
  
  // c) Preorden: Raíz - Izquierda - Derecha
  function preordenIterativo(raiz) {
    if (!raiz) return;
    let stack = [raiz];
    while (stack.length > 0) {
      let nodo = stack.pop();
      console.log(nodo.dato);
      if (nodo.der) stack.push(nodo.der);
      if (nodo.izq) stack.push(nodo.izq);
    }
  }
  