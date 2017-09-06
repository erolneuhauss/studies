require 'spec_helper'
describe 'apache' do
  context 'with default values for all parameters' do
    it { should contain_class('apache') }
    it { should contain_package('apache2') }
  end
end
