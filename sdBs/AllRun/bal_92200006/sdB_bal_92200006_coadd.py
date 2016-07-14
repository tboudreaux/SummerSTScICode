from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[321.635417,12.448056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_bal_92200006/sdB_bal_92200006_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_bal_92200006/sdB_bal_92200006_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()