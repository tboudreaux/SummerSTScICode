from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[199.745333,0.59175],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_131858.88+003530.3/sdB_SDSSJ910_131858.88+003530.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_131858.88+003530.3/sdB_SDSSJ910_131858.88+003530.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
