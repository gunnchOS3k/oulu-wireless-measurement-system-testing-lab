from oulu_measurement.packet_loss import loss_rate

def test_loss():
    assert loss_rate(100,5)==0.05
