from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[134.933833,50.680778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sbss_0856+508/sdB_sbss_0856+508_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sbss_0856+508/sdB_sbss_0856+508_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
