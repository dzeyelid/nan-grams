export interface Ingredient {
  id: string;
  name: string;
  gramPerTablespoon: number;
  gramPerTeaspoon: number;
  tags: string[];
  notes?: string;
}
