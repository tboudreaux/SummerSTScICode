from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[320.175083,38.898169],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KPD_2118+3841/sdB_KPD_2118+3841_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KPD_2118+3841/sdB_KPD_2118+3841_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
