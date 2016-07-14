from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[294.1375,52.755278],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_O11_J193633+524519/sdB_O11_J193633+524519_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_O11_J193633+524519/sdB_O11_J193633+524519_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
