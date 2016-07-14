from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[213.992458,-2.453972],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_141558.19-022714.3/sdB_SDSSJ910_141558.19-022714.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_141558.19-022714.3/sdB_SDSSJ910_141558.19-022714.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()