from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[276.0,51.923611],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_O11_J182400+515525/sdB_O11_J182400+515525_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_O11_J182400+515525/sdB_O11_J182400+515525_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
