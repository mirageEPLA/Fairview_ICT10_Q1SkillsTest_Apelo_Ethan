def create_order (event):

    #Get all checked coffee items
    coffees = document.querySelectorAll(".coffee")

    subtotal = 0
    selected_items = []

    for coffee.checked:
        name = coffee.getAttribute("data-name")
        price = float(coffee.getAttribute("data-price"))

        subtotal += price

        selected_items.append(f"{name} - Php{price:.2f}")

    # Calculate 12% tax
    tax = subtotal * 0.12

    #Calculate total
    total = subtotal + tax

    # Display selected products
    items_display = document.getElementById("selected-items")

    if selected_items:
        items_display.innerHTML = ("<strong>Selected Products:</strong><br>" + "<br>".join(selected_items))
    else:
        items_display.innerHTML= "No products selected."

    #Display receipt
    document.getElementById("subtotal").innerText = f"{subtotal:.2f}"
     document.getElementById("tax").innerText = f"{tax:.2f}"
      document.getElementById("total").innerText = f"{total:.2f}"
      </script>

      </body>
      </html>