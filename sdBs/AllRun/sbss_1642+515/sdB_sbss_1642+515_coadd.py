from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[250.878167,51.416056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sbss_1642+515/sdB_sbss_1642+515_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sbss_1642+515/sdB_sbss_1642+515_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
