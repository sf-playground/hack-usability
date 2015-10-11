# Angle brackets: < and >

## Common uses

- html-tags (`<tag>`)
- comparison operator (`<`, `>`, `<=`, `>=`)
- bitwise operator (`>>`, `<<`)
- part of an arrow (`->`, `=>`); always facing right?
- part of regular expressions in look behinds
- as a character to indicate a quote (markdown)
- as a character to indicate a direct descendent (css)

## Usability considerations

- vertically aligned with [dash](/cases/dash.md)
- vertically aligned with [equals-sign](/cases/equals-sign.md)
- 'openness' in relation to x-height
- when part of an arrow, it should feel 'connected' to the arrow, not to the context
- general: vertical alignment of [mathematical](/cases/mathematics.md) operators

## Comments and issues

- @burodepeper: I think the angle brackets in html-tags are too tight to the tag horizontally
- @burodepeper: I think angle brackets could use a little more vertical openness to increase the general sense of being a bracket/being a 'container'.

## Examples

### CSS

```css
div.container > p {
  font-style: italic;
}

div.container>p{font-style:italic;}
```

### HTML

```html
<div class='container'>
  <p>I am a paragraph</p>
</div>
```

### Javascript

```javascript
function inRange (value, low, high) {
  return (value >= low) && (value <= high);
}

function inRangeMinified(value,low,high){
  return (value>=low)&&(value<=high);
}
```

```coffeescript
inRange: (value, low = 0, high = 100) ->
  (value >= low) and (value <= high)
```

### Markdown

```markdown
> I am a quote by an important person.
```

### PHP

```php
$object = new StdClass();
$object->key = "value";

echo $methodsAndVariables->areOften()->chained()->likeThis;
```
