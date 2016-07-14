from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[336.467917,-9.999017],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_bps_cs22886-65/sdB_bps_cs22886-65_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_bps_cs22886-65/sdB_bps_cs22886-65_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
