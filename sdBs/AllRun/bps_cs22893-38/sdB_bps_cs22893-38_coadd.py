from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[346.031375,-8.940781],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_bps_cs22893-38/sdB_bps_cs22893-38_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_bps_cs22893-38/sdB_bps_cs22893-38_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
