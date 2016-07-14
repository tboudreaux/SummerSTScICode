from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[231.012625,1.572822],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_bps_cs22890-74/sdB_bps_cs22890-74_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_bps_cs22890-74/sdB_bps_cs22890-74_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
