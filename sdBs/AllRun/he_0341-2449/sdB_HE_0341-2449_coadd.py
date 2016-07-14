from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[55.901417,-24.663056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HE_0341-2449/sdB_HE_0341-2449_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HE_0341-2449/sdB_HE_0341-2449_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
