-- Moving between windows
vim.keymap.set({"n", "t"}, "<C-h>", "<cmd>wincmd h<CR>", { desc = "Move to the left window" })
vim.keymap.set({"n", "t"}, "<C-j>", "<cmd>wincmd j<CR>", { desc = "Move to the bottom window" })
vim.keymap.set({"n", "t"}, "<C-k>", "<cmd>wincmd k<CR>", { desc = "Move to the top window" })
vim.keymap.set({"n", "t"}, "<C-l>", "<cmd>wincmd l<CR>", { desc = "Move to the right window" })

-- Resize window
vim.keymap.set("n", "<C-Up>", "<cmd>resize +2<CR>", { desc = "Increase window height" })
vim.keymap.set("n", "<C-Down>", "<cmd>resize -2<CR>", { desc = "Decrease window height" })
vim.keymap.set("n", "<C-Left>", "<cmd>vertical resize -2<CR>", { desc = "Decrease window width" })
vim.keymap.set("n", "<C-Right>", "<cmd>vertical resize +2<CR>", { desc = "Increase window width" })

-- Diagnostic keymaps
vim.keymap.set("n", "<leader>e", vim.diagnostic.open_float, { desc = "Show diagnostics in a floating window" })

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
