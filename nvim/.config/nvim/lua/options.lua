-- Assign leader key
vim.g.mapleader = " "
vim.g.maplocalleader = " "

-- Make line numbers default
vim.opt.number = true
vim.opt.relativenumber = true

-- Enable mouse mode
vim.opt.mouse = "a"

-- Sync clipboard between OS and Neovim
vim.schedule(function()
	vim.opt.clipboard = "unnamedplus"
end)

-- Enable break indent
vim.opt.breakindent = true

-- Save undo history
vim.opt.undofile = true

-- Enable case-insensitive searching
vim.opt.ignorecase = true
vim.opt.smartcase = true

-- Keep signcolumn on by default
vim.opt.signcolumn = "yes"

-- Set update time
vim.opt.updatetime = 50

-- Configure how splits should be opened
vim.opt.splitright = true
vim.opt.splitbelow = true

-- Set minimal number of lines to keep above and below the cursor
vim.opt.scrolloff = 8

-- Set highlight on search
vim.opt.hlsearch = false
vim.opt.incsearch = true

-- Set indentation
vim.opt.autoindent = true
vim.opt.tabstop = 4
vim.opt.softtabstop = 4
vim.opt.shiftwidth = 4
vim.opt.smarttab = true

-- Disable line wrapping
vim.opt.wrap = false

-- Set colour column
vim.opt.colorcolumn = "80"

-- Enable backup
vim.opt.backup = false

-- Use a swapfile for the buffer
vim.opt.swapfile = false

-- Enable terminal colours
vim.opt.termguicolors = true
