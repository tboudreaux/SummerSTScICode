from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[142.527417,31.716667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ton_425/sdB_ton_425_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ton_425/sdB_ton_425_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
