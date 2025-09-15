import React, { useState } from 'react'
import {Popover, Button, Portal, SimpleGrid, Box, Text, Table} from "@chakra-ui/react"

const Plot = ({text}) => {
  return (
    <Popover.Root>
      <Popover.Trigger asChild>
        <Button size="sm">
          <Text textStyle="xl">{text}</Text>
        </Button>
      </Popover.Trigger>
      <Portal>
        <Popover.Positioner>
          <Popover.Content>
            <Popover.Arrow />
            <Popover.Body>
              <Popover.Title fontWeight="medium" textStyle="xl">Select the suitable plot</Popover.Title>
              <SimpleGrid columns={2} gap="40px">
                <Box bg="white">H</Box>
                <Box bg="white">E</Box>
                <Box bg="white">L</Box>
                <Box bg="white">O</Box>
              </SimpleGrid>
            </Popover.Body>
          </Popover.Content>
        </Popover.Positioner>
      </Portal>
    </Popover.Root>
  )
}

const Navbar = () => {
  return (
    <div>
      <Plot text="Plot" />
    </div>
  )
}

const DataFrame = () => {
  const [items, setItems] = useState([
    {id: 1, name: "Laptop", category: "Electronics", price: 999.99}
  ]);
  return (
    <div className="w-[400px] h-[200px] overflow-auto">
      <Table.Root size="sm">
        <Table.Header bg="white">
          <Table.Row>
            <Table.ColumnHeader>Product</Table.ColumnHeader>
            <Table.ColumnHeader>Category</Table.ColumnHeader>
            <Table.ColumnHeader textAlign="end">Price</Table.ColumnHeader>
          </Table.Row>
        </Table.Header>
        <Table.Body>
          {items.map((item) => (
            <Table.Row key={item.id}>
              <Table.Cell>{item.name}</Table.Cell>
              <Table.Cell>{item.category}</Table.Cell>
              <Table.Cell>{item.price}</Table.Cell>
            </Table.Row>
          ))}
        </Table.Body>
      </Table.Root>
    </div>
  )
}

const App = () => {
  return (
    <div style={{ background: "white", color: "black", minHeight: "100vh" }}>
      <Navbar />
      <div>
        <DataFrame />
      </div>
    </div>
  )
}

export default App