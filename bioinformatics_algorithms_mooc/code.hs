patternSearch [], pattern = 0 
patternSearch (x:xs), pattern = 

main = do
  putStrLn("Enter text:")
  text <- getLine
  putStrLn("Enter pattern:")
  pattern <- getLine

  putStrLn("Hey: " ++ text)
