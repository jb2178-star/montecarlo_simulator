from datastructures import BST
def get_portfolio_values(self):#get all portfolio values from LinkedList
        values = []
        current = self.value_history.head 
        while current:
            values.append(current.data)
            current = current.next
        return values
def get_portfolio_change(self):
        values = self.get_portfolio_val()
        if len(values) == 0:
            return "Portfolio is empty"
        elif len(values) == 1:#only initial value, no change to show
            initial_value = values[0]
            return {
                "Initial Value": f"${initial_value:,.2f}",
                "Current Value": f"${initial_value:,.2f}",
                "Total Change": "$0.00",
                "Percent Change": "0.00%",
            }
        else:
            initial_value = values[0]
            current_value = values[-1]
            if initial_value == 0:
                return f"Current Value: ${current_value:,.2f}"
            total_change = current_value - initial_value
            percent_change = (total_change / initial_value) * 100
            return {
                "Initial Value": f"${initial_value:,.2f}",
                "Current Value": f"${current_value:,.2f}",
                "Total Change": f"${total_change:+,.2f}",
                "Percent Change": f"{percent_change:+.2f}%",
            }
def get_stock_rankings(self): #BST finding best performing stocks
        sorted_stocks = self.price_tree.inorder_traversal()  #BST inorder traversal
        return sorted_stocks
def update_returns_tree(self):
        self.returns_tree = BST()  #reset the tree
        for bucket in self.simulated_returns.table:
            for ticker, returns in bucket:
                cumulative_return = 1.0 #calculate cumulative return (compound)
                for r in returns:
                    cumulative_return *= (1 + r)
                cumulative_return -= 1
                self.returns_tree.insert(ticker, cumulative_return)
def get_stock_rankings_by_return(self):
        self.update_returns_tr()
        return self.returns_tree.inorder_traversal()  #returns sorted (ticker, return)
def merge_sort_stocks(stocks, key_index=1):
        if len(stocks) <= 1:
            return stocks
        mid = len(stocks) // 2
        left = merge_sort_stocks(stocks[:mid], key_index)
        right = merge_sort_stocks(stocks[mid:], key_index)
        return _merger(left, right, key_index)

def _merger(left, right, key_index):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i][key_index] >= right[j][key_index]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result


