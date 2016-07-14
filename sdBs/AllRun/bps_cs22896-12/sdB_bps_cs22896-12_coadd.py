from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[290.609125,-55.867922],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_bps_cs22896-12/sdB_bps_cs22896-12_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_bps_cs22896-12/sdB_bps_cs22896-12_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
