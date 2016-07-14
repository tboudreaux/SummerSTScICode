from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[108.62425,22.283389],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_uvo_0711+22/sdB_uvo_0711+22_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_uvo_0711+22/sdB_uvo_0711+22_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
