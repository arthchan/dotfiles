-- Moving between panes
vim.keymap.set({"n", "t"}, "<C-h>", "<cmd>wincmd h<CR>", { desc = "Move to the left pane" })
vim.keymap.set({"n", "t"}, "<C-j>", "<cmd>wincmd j<CR>", { desc = "Move to the bottom pane" })
vim.keymap.set({"n", "t"}, "<C-k>", "<cmd>wincmd k<CR>", { desc = "Move to the top pane" })
vim.keymap.set({"n", "t"}, "<C-l>", "<cmd>wincmd l<CR>", { desc = "Move to the right pane" })

-- Resize pane
vim.keymap.set("n", "<C-Up>", "<cmd>resize +2<CR>", { desc = "Increase pane height" })
vim.keymap.set("n", "<C-Down>", "<cmd>resize -2<CR>", { desc = "Decrease pane height" })
vim.keymap.set("n", "<C-Left>", "<cmd>vertical resize -2<CR>", { desc = "Decrease pane width" })
vim.keymap.set("n", "<C-Right>", "<cmd>vertical resize +2<CR>", { desc = "Increase pane width" })

-- Disable arrow keys in normal mode
vim.keymap.set("n", "<left>", '<cmd>echo "Use h to move!!"<CR>', { desc = "Disable left arrow key" })
vim.keymap.set("n", "<right>", '<cmd>echo "Use l to move!!"<CR>', { desc = "Disable right arrow key" })
vim.keymap.set("n", "<up>", '<cmd>echo "Use k to move!!"<CR>', { desc = "Disable up arrow key" })
vim.keymap.set("n", "<down>", '<cmd>echo "Use j to move!!"<CR>', { desc = "Disable down arrow key" })

-- Escape from insert mode
vim.keymap.set("i", "<C-c>", "<Esc>", { desc = "Escape from insert mode" })

-- Moving hightlighted line up and down
vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv", { desc = "Move highlighted line down" })
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv", { desc = "Move highlighted line up" })

-- Indent highlighted line left and right
vim.keymap.set("v", "<", "<gv", { desc = "Indent highlighted line to the left" })
vim.keymap.set("v", ">", ">gv", { desc = "Indent highlighted line to the right" })

-- LSP keymaps
vim.keymap.set({ "n", "v" }, "<leader>la", vim.lsp.buf.code_action, { desc = "LSP: Execute code action" })
vim.keymap.set("n", "<leader>lc", vim.lsp.buf.declaration, { desc = "LSP: Go to declaration" })
vim.keymap.set("n", "<leader>ld", vim.lsp.buf.definition, { desc = "LSP: Go to definition" })
vim.keymap.set("n", "<leader>lf", vim.lsp.buf.format, { desc = "LSP: Format code" })
vim.keymap.set("n", "<leader>lh", vim.lsp.buf.rename, { desc = "LSP: Rename variable" })
vim.keymap.set("n", "<leader>li", vim.lsp.buf.implementation, { desc = "LSP: Go to implementation" })
vim.keymap.set("n", "<leader>lk", vim.lsp.buf.hover, { desc = "LSP: Display hover information" })
vim.keymap.set("n", "<leader>lr", vim.lsp.buf.references, { desc = "LSP: Go to references" })
vim.keymap.set("n", "<leader>ls", vim.lsp.buf.workspace_symbol, { desc = "LSP: Search workspace symbols" })
vim.keymap.set("n", "<leader>lt", vim.lsp.buf.type_definition, { desc = "LSP: Go to type definition" })
