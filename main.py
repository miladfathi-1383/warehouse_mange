def main_menu():
    print('=' * 40)
    print('      WAREHOUSE MANAGEMENT SYSTEM')
    print('=' * 40)

    print('1. Product Management')
    print('2. Inventory Management')
    print('3. Supplier Management')
    print('4. Customer Management')
    print('5. Purchase Order Management')
    print('6. Sales Order Management')
    print('7. Reports')
    print('8. User Management')
    print('9. Settings')
    print('10. Exit')


def product_management_menu():
    print('=' * 40)
    print('          PRODUCT MANAGEMENT')
    print('=' * 40)
    print('1.Add New Product')
    print('2.View All Products')
    print('3.Search for a Product')
    print('4.Update Product Information')
    print('5.Delete Product')
    print('6.Back to Main Menu')


def inventory_management_menu():
    print('=' * 40)
    print('          INVENTORY MANAGEMENT')
    print('=' * 40)
    print('1.Stock In')
    print('2.Stock Out')
    print('3.View Current Stock')
    print('4.View Transaction History')
    print('5.View Low-Stock Products')
    print('6.Search Inventory')
    print('7.Back to Main Menu')


def supplier_management_menu():
    print('=' * 40)
    print('          SUPPLIER MANAGEMENT')
    print('=' * 40)
    print('1.Add New Supplier')
    print('2.View All Suppliers')
    print('3.Search for a Supplier')
    print('4.Update Supplier Information')
    print('5.Delete Supplier')
    print('6.Back to Main Menu')


def customer_management_menu():
    print('=' * 40)
    print('          CUSTOMER MANAGEMENT')
    print('=' * 40)
    print('1. Add New Customer')
    print('2. View All Customers')
    print('3. Search for a Customer')
    print('4. Update Customer Information')
    print('5. Delete Customer')
    print('6. Customer History')
    print('7. Back to Main Menu')


def purchase_order_management_menu():
    print('=' * 40)
    print('       PURCHASE ORDER MANAGEMENT')
    print('=' * 40)
    print('1. Create Purchase Order')
    print('2. View All Purchase Orders')
    print('3. Search for a Purchase Order')
    print('4. Receive Purchased Items')
    print('5. Cancel Purchase Order')
    print('6. Back to Main Menu')


def sales_order_management_menu():
    print('=' * 40)
    print('          SALES ORDER MANAGEMENT')
    print('=' * 40)
    print('1. Create Sales Order')
    print('2. View All Sales Orders')
    print('3. Search for a Sales Order')
    print('4. Process Sales Order')
    print('5. Cancel Sales Order')
    print('6. Back to Main Menu')


def report_menu():
    print('=' * 40)
    print('                 REPORTS')
    print('=' * 40)
    print('1.Inventory Report')
    print('2.Stock Movement Report')
    print('3.Low-Stock Report')
    print('4.Purchase Report')
    print('5.Sales Report')
    print('6.Inventory Valuation Report')
    print('7.Product Performance Report')
    print('8.Back to Main Menu')


def user_management_menu():
    print('=' * 40)
    print('             USER MANAGEMENT')
    print('=' * 40)
    print('1.Ad New User')
    print('2.View All Users')
    print('3.Search for a User')
    print('4.Update User Information')
    print('5.Manage User Roles')
    print('6.Deactivate User')
    print('7Back to Main Menu')


def settings_menu():
    print('=' * 40)
    print('                 SETTINGS')
    print('=' * 40)
    print('1.Database Connection')
    print('2.Export Data')
    print('3.Backup Database')
    print('4.Restore Database')
    print('5.Back to Main Menu')


while True:
    main_menu()
    choice = input('Your choice: ').strip()

    if choice == '1':
        product_management_menu()

    elif choice == '2':
        inventory_management_menu()

    elif choice == '3':
        supplier_management_menu()

    elif choice == '4':
        customer_management_menu()

    elif choice == '5':
        purchase_order_management_menu()

    elif choice == '6':
        sales_order_management_menu()

    elif choice == '7':
        report_menu()

    elif choice == '8':
        user_management_menu()

    elif choice == '9':
        settings_menu()

    elif choice == '10':
        print('Exiting Warehouse Management System...')
        break

    else:
        print('Invalid choice! Please enter a number between 1 and 10.')
